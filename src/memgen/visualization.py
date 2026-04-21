"""Build a self-contained HTML viewer for a single memgen result set."""

from __future__ import annotations

import html
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

STAGE_ORDER = ("generation", "scoring", "memory", "evaluation")
STAGE_FILES = {
    "generation": ("generations", "generations.jsonl"),
    "scoring": ("scores", "scores.jsonl"),
    "memory": ("memories", "memories.jsonl"),
    "evaluation": ("evaluations", "evaluations.jsonl"),
}
HTML_FILENAME = "visualization.html"
DOMAIN_PLOTS_HTML_FILENAME = "domain_plots.html"
DOMAIN_PLOT_FILES = {
    "counts": "domain_counts.svg",
    "rates": "domain_pass_rates.svg",
    "improvement": "domain_improvement.svg",
}
DOMAIN_ORDER = ("math", "coding", "science", "logic", "simulation", "table")
DOMAIN_LABELS = {
    "math": "Math",
    "coding": "Coding",
    "science": "Science",
    "logic": "Logic",
    "simulation": "Simulation",
    "table": "Table",
}


def build_visualization_data(results_path: str | Path) -> dict[str, Any]:
    root = Path(results_path).expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"Result path is not a directory: {root}")

    stage_records = {
        stage: _load_stage_records(root, *location)
        for stage, location in STAGE_FILES.items()
    }
    artifacts = _load_artifacts(root)
    artifact_index = _load_artifact_index(root)

    if not any(stage_records.values()) and not artifacts and not artifact_index:
        raise ValueError(
            f"No memgen artifacts or stage files found under {root}. "
            "Expected directories like generations/, scores/, memories/, evaluations/, or artifacts/."
        )

    problem_ids: set[str] = set()
    for records in stage_records.values():
        problem_ids.update(records)
    problem_ids.update(artifacts)
    problem_ids.update(artifact_index)

    inferred_domain = _infer_domain(root)
    problems = []
    for problem_id in sorted(problem_ids, key=_natural_sort_key):
        artifact_entry = artifacts.get(problem_id)
        artifact = artifact_entry["data"] if artifact_entry else {}
        index_entry = artifact_index.get(problem_id, {})

        stages = {
            stage: value
            for stage, value in (artifact.get("stages") or {}).items()
            if stage in STAGE_ORDER
        }
        for stage, records in stage_records.items():
            if problem_id in records and stage not in stages:
                stages[stage] = records[problem_id]
        for stage in index_entry.get("stages", []):
            stages.setdefault(stage, {})

        available_stages = [stage for stage in STAGE_ORDER if stage in stages]
        generation = stages.get("generation") or {}
        scoring = stages.get("scoring") or {}
        memory = stages.get("memory") or {}
        evaluation = stages.get("evaluation") or {}
        score_summary = _summarize_scores(scoring.get("scores") or [])
        links = _build_links(artifact_entry["path"]) if artifact_entry else {}

        problems.append(
            {
                "problem_id": problem_id,
                "domain": artifact.get("domain") or index_entry.get("domain") or inferred_domain,
                "problem": artifact.get("problem") or {},
                "stages": stages,
                "available_stages": available_stages,
                "stage_count": len(available_stages),
                "generation_count": len(generation.get("solutions") or []),
                "memory_item_count": len(memory.get("items") or []),
                "memory_skipped": memory.get("skipped"),
                "score_summary": score_summary,
                "baseline_pass_rate": evaluation.get("baseline_pass_rate"),
                "augmented_pass_rate": evaluation.get("augmented_pass_rate"),
                "improvement": evaluation.get("improvement", index_entry.get("improvement")),
                "links": links,
            }
        )

    return {
        "title": f"Memgen Viewer: {root.name}",
        "results_path": str(root),
        "result_name": _display_name(root),
        "domain": inferred_domain,
        "problem_count": len(problems),
        "stage_order": list(STAGE_ORDER),
        "summary": _build_summary(problems),
        "problems": problems,
    }


def render_visualization_html(data: dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>__TITLE__</title>
  <style>
    :root {
      --bg: #f4efe5;
      --paper: rgba(255, 252, 246, 0.9);
      --panel: rgba(255, 255, 255, 0.76);
      --panel-strong: rgba(255, 255, 255, 0.92);
      --line: rgba(48, 58, 79, 0.16);
      --ink: #1f2430;
      --muted: #5e6573;
      --accent: #0f766e;
      --accent-soft: rgba(15, 118, 110, 0.12);
      --good: #18794e;
      --good-soft: rgba(24, 121, 78, 0.14);
      --warn: #b45309;
      --warn-soft: rgba(180, 83, 9, 0.14);
      --bad: #b42318;
      --bad-soft: rgba(180, 35, 24, 0.12);
      --shadow: 0 18px 40px rgba(31, 36, 48, 0.08);
      --mono: "IBM Plex Mono", "SFMono-Regular", "Menlo", monospace;
      --sans: "Avenir Next", "Segoe UI", "Helvetica Neue", sans-serif;
    }

    * {
      box-sizing: border-box;
    }

    html, body {
      margin: 0;
      min-height: 100%;
      background:
        radial-gradient(circle at top left, rgba(15, 118, 110, 0.18), transparent 28%),
        radial-gradient(circle at bottom right, rgba(180, 83, 9, 0.12), transparent 28%),
        linear-gradient(180deg, #faf6ee 0%, #f0e7d7 100%);
      color: var(--ink);
      font-family: var(--sans);
    }

    body {
      min-height: 100vh;
    }

    a {
      color: var(--accent);
    }

    button,
    input,
    select {
      font: inherit;
    }

    .page {
      display: grid;
      grid-template-columns: 320px minmax(0, 1fr);
      min-height: 100vh;
    }

    .sidebar {
      position: sticky;
      top: 0;
      height: 100vh;
      padding: 24px 20px;
      background: rgba(255, 248, 238, 0.78);
      border-right: 1px solid var(--line);
      backdrop-filter: blur(18px);
      overflow: auto;
    }

    .main {
      padding: 28px;
      overflow: auto;
    }

    .brand {
      margin-bottom: 20px;
    }

    .eyebrow {
      margin: 0 0 6px;
      font-size: 12px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--muted);
    }

    .brand h1,
    .section-title,
    .panel h2 {
      margin: 0;
      font-weight: 700;
      letter-spacing: -0.03em;
    }

    .brand h1 {
      font-size: 28px;
      line-height: 1.05;
    }

    .path-block {
      margin-top: 12px;
      padding: 12px 14px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 14px;
      box-shadow: var(--shadow);
      font-size: 13px;
      color: var(--muted);
    }

    .path-block code {
      display: block;
      margin-top: 4px;
      font-family: var(--mono);
      font-size: 12px;
      color: var(--ink);
      word-break: break-word;
    }

    .sidebar-section {
      margin-top: 24px;
    }

    .sidebar-label {
      display: block;
      margin-bottom: 8px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
    }

    .control,
    .select {
      width: 100%;
      padding: 12px 14px;
      border-radius: 12px;
      border: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.92);
      color: var(--ink);
      box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.6);
    }

    .summary-grid {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 14px;
      margin-bottom: 18px;
    }

    .card,
    .panel {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 18px;
      box-shadow: var(--shadow);
    }

    .card {
      padding: 18px;
    }

    .metric-label {
      margin: 0 0 10px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
    }

    .metric-value {
      margin: 0;
      font-size: 30px;
      line-height: 1;
      letter-spacing: -0.04em;
    }

    .metric-detail {
      margin: 8px 0 0;
      color: var(--muted);
      font-size: 14px;
    }

    .problem-list {
      display: grid;
      gap: 10px;
      margin-top: 14px;
    }

    .problem-button {
      width: 100%;
      padding: 14px;
      text-align: left;
      background: var(--panel);
      border: 1px solid transparent;
      border-radius: 16px;
      color: var(--ink);
      cursor: pointer;
      transition: transform 140ms ease, border-color 140ms ease, background 140ms ease;
    }

    .problem-button:hover,
    .problem-button:focus-visible {
      transform: translateY(-1px);
      border-color: rgba(15, 118, 110, 0.3);
      outline: none;
    }

    .problem-button.active {
      background: linear-gradient(180deg, rgba(15, 118, 110, 0.16), rgba(255, 255, 255, 0.9));
      border-color: rgba(15, 118, 110, 0.34);
    }

    .problem-header,
    .row-between {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: flex-start;
    }

    .problem-id {
      font-weight: 700;
      letter-spacing: -0.02em;
    }

    .problem-snippet {
      margin: 8px 0 10px;
      font-size: 13px;
      color: var(--muted);
      line-height: 1.5;
    }

    .chip-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .chip,
    .stage-chip,
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 9px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      line-height: 1;
      white-space: nowrap;
    }

    .chip {
      background: rgba(48, 58, 79, 0.08);
      color: var(--muted);
    }

    .stage-chip.on {
      background: var(--accent-soft);
      color: var(--accent);
    }

    .stage-chip.off {
      background: rgba(48, 58, 79, 0.08);
      color: var(--muted);
    }

    .badge.good {
      background: var(--good-soft);
      color: var(--good);
    }

    .badge.bad {
      background: var(--bad-soft);
      color: var(--bad);
    }

    .badge.warn {
      background: var(--warn-soft);
      color: var(--warn);
    }

    .badge.neutral {
      background: rgba(48, 58, 79, 0.08);
      color: var(--muted);
    }

    .panel {
      padding: 20px;
    }

    .panel + .panel {
      margin-top: 16px;
    }

    .section-title {
      font-size: 24px;
      margin-bottom: 6px;
    }

    .section-subtitle {
      margin: 0 0 18px;
      color: var(--muted);
      line-height: 1.5;
    }

    .tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 18px;
    }

    .tab-button {
      padding: 10px 14px;
      border-radius: 999px;
      border: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.84);
      color: var(--muted);
      cursor: pointer;
      transition: border-color 140ms ease, color 140ms ease, background 140ms ease;
    }

    .tab-button.active {
      border-color: rgba(15, 118, 110, 0.34);
      background: var(--accent-soft);
      color: var(--accent);
    }

    .tab-button.dimmed {
      opacity: 0.68;
    }

    .two-col {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
    }

    .three-col {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
    }

    .table-wrap {
      overflow: auto;
      border: 1px solid var(--line);
      border-radius: 14px;
      background: var(--panel-strong);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
    }

    th,
    td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--line);
      text-align: left;
      vertical-align: top;
    }

    th {
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      background: rgba(255, 255, 255, 0.84);
      position: sticky;
      top: 0;
    }

    tr:last-child td {
      border-bottom: none;
    }

    .bar-list {
      display: grid;
      gap: 12px;
    }

    .bar-row {
      display: grid;
      gap: 8px;
    }

    .bar-meta {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      color: var(--muted);
      font-size: 14px;
    }

    .bar-track {
      height: 10px;
      border-radius: 999px;
      background: rgba(48, 58, 79, 0.08);
      overflow: hidden;
    }

    .bar-fill {
      height: 100%;
      border-radius: inherit;
      background: linear-gradient(90deg, #0f766e, #38b2ac);
    }

    .empty {
      padding: 20px;
      border-radius: 14px;
      background: rgba(48, 58, 79, 0.05);
      color: var(--muted);
    }

    .note {
      margin-top: 12px;
      padding: 12px 14px;
      border-radius: 14px;
      background: rgba(15, 118, 110, 0.08);
      color: var(--accent);
    }

    .details-card {
      overflow: hidden;
    }

    details summary {
      list-style: none;
      cursor: pointer;
    }

    details summary::-webkit-details-marker {
      display: none;
    }

    .details-summary {
      display: grid;
      gap: 10px;
    }

    pre,
    code {
      font-family: var(--mono);
    }

    pre {
      margin: 0;
      white-space: pre-wrap;
      word-break: break-word;
      background: rgba(31, 36, 48, 0.96);
      color: #f6f3ee;
      border-radius: 14px;
      padding: 14px;
      font-size: 12px;
      line-height: 1.55;
      overflow: auto;
    }

    .inline-code {
      display: inline-block;
      padding: 2px 6px;
      border-radius: 8px;
      background: rgba(31, 36, 48, 0.08);
      font-family: var(--mono);
      font-size: 12px;
    }

    .stack {
      display: grid;
      gap: 14px;
    }

    .kv-grid {
      display: grid;
      gap: 12px;
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .kv-card {
      padding: 14px;
      border-radius: 14px;
      background: rgba(255, 255, 255, 0.86);
      border: 1px solid var(--line);
    }

    .kv-card strong {
      display: block;
      margin-bottom: 8px;
      font-size: 12px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
    }

    .list-clean {
      margin: 0;
      padding-left: 18px;
    }

    .list-clean li + li {
      margin-top: 8px;
    }

    .muted {
      color: var(--muted);
    }

    @media (max-width: 1120px) {
      .summary-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }

      .two-col,
      .three-col,
      .kv-grid {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 900px) {
      .page {
        grid-template-columns: 1fr;
      }

      .sidebar {
        position: static;
        height: auto;
        border-right: none;
        border-bottom: 1px solid var(--line);
      }

      .main {
        padding: 18px;
      }
    }
  </style>
</head>
<body>
  <div class="page">
    <aside class="sidebar">
      <div class="brand">
        <p class="eyebrow">Memgen Results Viewer</p>
        <h1 id="brand-title"></h1>
        <div class="path-block">
          Focused Result Set
          <code id="result-path"></code>
        </div>
      </div>

      <div class="sidebar-section">
        <label class="sidebar-label" for="problem-search">Search Problems</label>
        <input id="problem-search" class="control" type="search" placeholder="Filter by id or statement">
      </div>

      <div class="sidebar-section">
        <label class="sidebar-label" for="problem-sort">Sort Problems</label>
        <select id="problem-sort" class="select">
          <option value="problem_id">Problem ID</option>
          <option value="improvement_desc">Improvement, high to low</option>
          <option value="improvement_asc">Improvement, low to high</option>
          <option value="stage_count_desc">Most complete first</option>
        </select>
      </div>

      <div class="sidebar-section">
        <div class="row-between">
          <span class="sidebar-label" style="margin: 0;">Problems</span>
          <span id="problem-counter" class="chip"></span>
        </div>
        <div id="problem-list" class="problem-list"></div>
      </div>
    </aside>

    <main class="main">
      <section id="summary"></section>
      <section>
        <div id="view-tabs" class="tabs"></div>
        <div id="content"></div>
      </section>
    </main>
  </div>

  <script id="visualization-data" type="application/json">__DATA_JSON__</script>
  <script>
    const dataset = JSON.parse(document.getElementById("visualization-data").textContent);
    const STAGE_LABELS = {
      overview: "Overview",
      problem: "Problem",
      generation: "Generation",
      scoring: "Scoring",
      memory: "Memory",
      evaluation: "Evaluation",
    };
    const state = {
      query: "",
      sort: "problem_id",
      activeView: "overview",
      selectedProblemId: dataset.problems[0] ? dataset.problems[0].problem_id : null,
    };
    const problemsById = new Map(dataset.problems.map((problem) => [problem.problem_id, problem]));

    document.getElementById("brand-title").textContent = dataset.result_name;
    document.getElementById("result-path").textContent = dataset.results_path;

    document.getElementById("problem-search").addEventListener("input", (event) => {
      state.query = event.target.value.trim().toLowerCase();
      render();
    });

    document.getElementById("problem-sort").addEventListener("change", (event) => {
      state.sort = event.target.value;
      render();
    });

    function escapeHtml(value) {
      return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#39;");
    }

    function formatRate(value) {
      if (value === null || value === undefined || Number.isNaN(value)) {
        return "n/a";
      }
      return `${(value * 100).toFixed(1)}%`;
    }

    function formatDelta(value) {
      if (value === null || value === undefined || Number.isNaN(value)) {
        return "n/a";
      }
      const percent = value * 100;
      return `${percent >= 0 ? "+" : ""}${percent.toFixed(1)} pts`;
    }

    function scoreBadgeClass(score, tier) {
      if (score === null || score === undefined) {
        return "neutral";
      }
      if (score >= 1 || ["correct", "full"].includes(tier)) {
        return "good";
      }
      if (score > 0 || ["partial"].includes(tier)) {
        return "warn";
      }
      return "bad";
    }

    function improvementBadgeClass(value) {
      if (value === null || value === undefined) {
        return "neutral";
      }
      if (value > 0) {
        return "good";
      }
      if (value < 0) {
        return "bad";
      }
      return "neutral";
    }

    function summarizeText(text, limit = 140) {
      const normalized = String(text ?? "").replace(/\\s+/g, " ").trim();
      if (!normalized) {
        return "No statement captured.";
      }
      return normalized.length > limit ? `${normalized.slice(0, limit - 1)}…` : normalized;
    }

    function filteredProblems() {
      const query = state.query;
      const items = dataset.problems.filter((problem) => {
        if (!query) {
          return true;
        }
        const statement = problem.problem && problem.problem.statement ? problem.problem.statement : "";
        return `${problem.problem_id} ${statement}`.toLowerCase().includes(query);
      });

      items.sort((left, right) => {
        if (state.sort === "improvement_desc") {
          return compareNumbers(right.improvement, left.improvement) || naturalCompare(left.problem_id, right.problem_id);
        }
        if (state.sort === "improvement_asc") {
          return compareNumbers(left.improvement, right.improvement) || naturalCompare(left.problem_id, right.problem_id);
        }
        if (state.sort === "stage_count_desc") {
          return (right.stage_count - left.stage_count) || naturalCompare(left.problem_id, right.problem_id);
        }
        return naturalCompare(left.problem_id, right.problem_id);
      });

      return items;
    }

    function compareNumbers(left, right) {
      const a = left === null || left === undefined ? Number.NEGATIVE_INFINITY : left;
      const b = right === null || right === undefined ? Number.NEGATIVE_INFINITY : right;
      return a === b ? 0 : a < b ? -1 : 1;
    }

    function naturalCompare(left, right) {
      return left.localeCompare(right, undefined, { numeric: true, sensitivity: "base" });
    }

    function ensureSelection(items) {
      if (!items.length) {
        state.selectedProblemId = null;
        return null;
      }
      if (!state.selectedProblemId || !items.some((item) => item.problem_id === state.selectedProblemId)) {
        state.selectedProblemId = items[0].problem_id;
      }
      return problemsById.get(state.selectedProblemId);
    }

    function stageChip(stage, enabled) {
      return `<span class="stage-chip ${enabled ? "on" : "off"}">${escapeHtml(STAGE_LABELS[stage].slice(0, 3).toUpperCase())}</span>`;
    }

    function renderSummary() {
      const summary = dataset.summary;
      const cards = [
        {
          label: "Problems",
          value: dataset.problem_count,
          detail: `${summary.evaluation_count} evaluated`,
        },
        {
          label: "Mean Baseline",
          value: formatRate(summary.mean_baseline_pass_rate),
          detail: "avg@k across evaluated problems",
        },
        {
          label: "Mean Augmented",
          value: formatRate(summary.mean_augmented_pass_rate),
          detail: "avg@k with memory injection",
        },
        {
          label: "Mean Improvement",
          value: formatDelta(summary.mean_improvement),
          detail: `${summary.helped_count} helped, ${summary.hurt_count} hurt`,
        },
      ];

      document.getElementById("summary").innerHTML = `
        <div class="summary-grid">
          ${cards.map((card) => `
            <article class="card">
              <p class="metric-label">${escapeHtml(card.label)}</p>
              <p class="metric-value">${escapeHtml(card.value)}</p>
              <p class="metric-detail">${escapeHtml(card.detail)}</p>
            </article>
          `).join("")}
        </div>
      `;
    }

    function renderProblemList(items, selectedProblem) {
      const list = document.getElementById("problem-list");
      document.getElementById("problem-counter").textContent = `${items.length}/${dataset.problem_count}`;

      if (!items.length) {
        list.innerHTML = `<div class="empty">No problems match the current filter.</div>`;
        return;
      }

      list.innerHTML = items.map((problem) => {
        const statement = problem.problem && problem.problem.statement ? problem.problem.statement : "";
        const improvement = problem.improvement;
        const improvementText = improvement === null || improvement === undefined ? "no eval" : formatDelta(improvement);
        return `
          <button class="problem-button ${selectedProblem && selectedProblem.problem_id === problem.problem_id ? "active" : ""}" data-problem-id="${escapeHtml(problem.problem_id)}">
            <div class="problem-header">
              <span class="problem-id">${escapeHtml(problem.problem_id)}</span>
              <span class="badge ${improvementBadgeClass(improvement)}">${escapeHtml(improvementText)}</span>
            </div>
            <p class="problem-snippet">${escapeHtml(summarizeText(statement, 96))}</p>
            <div class="chip-row">
              ${dataset.stage_order.map((stage) => stageChip(stage, problem.available_stages.includes(stage))).join("")}
            </div>
          </button>
        `;
      }).join("");

      list.querySelectorAll("[data-problem-id]").forEach((button) => {
        button.addEventListener("click", () => {
          state.selectedProblemId = button.getAttribute("data-problem-id");
          if (state.activeView === "overview") {
            state.activeView = "problem";
          }
          render();
        });
      });
    }

    function renderTabs(problem) {
      const views = ["overview", "problem", ...dataset.stage_order];
      const container = document.getElementById("view-tabs");

      container.innerHTML = views.map((view) => {
        const hasStage = view === "overview" || view === "problem" || (problem && problem.available_stages.includes(view));
        return `
          <button class="tab-button ${state.activeView === view ? "active" : ""} ${hasStage ? "" : "dimmed"}" data-view="${view}">
            ${escapeHtml(STAGE_LABELS[view])}
          </button>
        `;
      }).join("");

      container.querySelectorAll("[data-view]").forEach((button) => {
        button.addEventListener("click", () => {
          state.activeView = button.getAttribute("data-view");
          render();
        });
      });
    }

    function infoCard(label, value, detail = "") {
      return `
        <div class="kv-card">
          <strong>${escapeHtml(label)}</strong>
          <div>${escapeHtml(value)}</div>
          ${detail ? `<div class="muted" style="margin-top: 6px;">${escapeHtml(detail)}</div>` : ""}
        </div>
      `;
    }

    function renderPromptPanel(title, prompt) {
      if (!prompt || (!prompt.system_prompt && !prompt.user_prompt)) {
        return `<div class="empty">No prompt captured for ${escapeHtml(title.toLowerCase())}.</div>`;
      }
      return `
        <section class="panel">
          <h2>${escapeHtml(title)} Prompt</h2>
          <div class="stack" style="margin-top: 14px;">
            ${prompt.system_prompt ? `<div><p class="metric-label">System</p><pre>${escapeHtml(prompt.system_prompt)}</pre></div>` : ""}
            ${prompt.user_prompt ? `<div><p class="metric-label">User</p><pre>${escapeHtml(prompt.user_prompt)}</pre></div>` : ""}
          </div>
        </section>
      `;
    }

    function renderSolutionCards(label, solutions, scores = []) {
      if (!solutions || !solutions.length) {
        return `<div class="empty">No ${escapeHtml(label.toLowerCase())} captured.</div>`;
      }

      return `
        <div class="stack">
          ${solutions.map((solution, index) => {
            const score = scores[index];
            const details = score && score.details ? `<div style="margin-top: 14px;"><p class="metric-label">Score Details</p><pre>${escapeHtml(JSON.stringify(score.details, null, 2))}</pre></div>` : "";
            return `
              <details class="card details-card">
                <summary class="details-summary">
                  <div class="row-between">
                    <span class="problem-id">${escapeHtml(`${label} ${index + 1}`)}</span>
                    ${score ? `<span class="badge ${scoreBadgeClass(score.score, score.tier)}">${escapeHtml(`${score.tier || "score"} ${Number(score.score ?? 0).toFixed(2)}`)}</span>` : ""}
                  </div>
                  <div class="muted">${escapeHtml(summarizeText(solution, 180))}</div>
                </summary>
                <div style="margin-top: 14px;">
                  <pre>${escapeHtml(solution)}</pre>
                  ${details}
                </div>
              </details>
            `;
          }).join("")}
        </div>
      `;
    }

    function renderScoreTable(scores) {
      if (!scores || !scores.length) {
        return `<div class="empty">No scores captured for this problem.</div>`;
      }
      return `
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Generation</th>
                <th>Score</th>
                <th>Tier</th>
                <th>Details</th>
              </tr>
            </thead>
            <tbody>
              ${scores.map((score) => `
                <tr>
                  <td>${escapeHtml(String((score.generation_index ?? 0) + 1))}</td>
                  <td>${escapeHtml(Number(score.score ?? 0).toFixed(2))}</td>
                  <td><span class="badge ${scoreBadgeClass(score.score, score.tier)}">${escapeHtml(score.tier || "n/a")}</span></td>
                  <td>${score.details ? `<span class="inline-code">${escapeHtml(JSON.stringify(score.details))}</span>` : "n/a"}</td>
                </tr>
              `).join("")}
            </tbody>
          </table>
        </div>
      `;
    }

    function renderOverview(items) {
      const summary = dataset.summary;
      const total = Math.max(dataset.problem_count, 1);
      return `
        <section class="panel">
          <h2 class="section-title">Overview</h2>
          <p class="section-subtitle">This view is scoped to one result-set path. Filter in the sidebar, then switch into generation, scoring, memory, or evaluation for a specific problem.</p>
          <div class="two-col">
            <div class="panel" style="margin: 0;">
              <h2>Stage Coverage</h2>
              <div class="bar-list" style="margin-top: 14px;">
                ${dataset.stage_order.map((stage) => {
                  const count = summary.stage_counts[stage] || 0;
                  const percent = Math.round((count / total) * 100);
                  return `
                    <div class="bar-row">
                      <div class="bar-meta">
                        <span>${escapeHtml(STAGE_LABELS[stage])}</span>
                        <span>${count}/${dataset.problem_count}</span>
                      </div>
                      <div class="bar-track"><div class="bar-fill" style="width: ${percent}%;"></div></div>
                    </div>
                  `;
                }).join("")}
              </div>
            </div>

            <div class="panel" style="margin: 0;">
              <h2>Evaluation Shape</h2>
              ${summary.evaluation_count ? `
                <div class="kv-grid" style="margin-top: 14px;">
                  ${infoCard("Helped", String(summary.helped_count), "positive improvement")}
                  ${infoCard("Hurt", String(summary.hurt_count), "negative improvement")}
                  ${infoCard("No Change", String(summary.no_change_count), "flat improvement")}
                  ${infoCard("Evaluated", String(summary.evaluation_count), "problems with evaluation output")}
                </div>
              ` : `<div class="empty" style="margin-top: 14px;">No evaluation records found in this result set.</div>`}
            </div>
          </div>
        </section>

        <section class="panel">
          <h2>Problem Table</h2>
          <div class="table-wrap" style="margin-top: 14px;">
            <table>
              <thead>
                <tr>
                  <th>Problem</th>
                  <th>Stages</th>
                  <th>Memory</th>
                  <th>Baseline</th>
                  <th>Augmented</th>
                  <th>Delta</th>
                </tr>
              </thead>
              <tbody>
                ${items.map((problem) => `
                  <tr>
                    <td>${escapeHtml(problem.problem_id)}</td>
                    <td>${escapeHtml(problem.available_stages.join(", ") || "none")}</td>
                    <td>${problem.memory_skipped === true ? "skipped" : problem.memory_item_count ? `${problem.memory_item_count} items` : "n/a"}</td>
                    <td>${escapeHtml(formatRate(problem.baseline_pass_rate))}</td>
                    <td>${escapeHtml(formatRate(problem.augmented_pass_rate))}</td>
                    <td><span class="badge ${improvementBadgeClass(problem.improvement)}">${escapeHtml(formatDelta(problem.improvement))}</span></td>
                  </tr>
                `).join("")}
              </tbody>
            </table>
          </div>
        </section>
      `;
    }

    function renderProblem(problem) {
      if (!problem) {
        return `<section class="panel"><div class="empty">No problem selected.</div></section>`;
      }

      const metadata = problem.problem && problem.problem.metadata ? problem.problem.metadata : null;
      const links = problem.links || {};
      return `
        <section class="panel">
          <h2 class="section-title">${escapeHtml(problem.problem_id)}</h2>
          <p class="section-subtitle">${escapeHtml(summarizeText(problem.problem.statement || "No problem statement captured.", 320))}</p>
          <div class="kv-grid">
            ${infoCard("Domain", problem.domain || dataset.domain || "unknown")}
            ${infoCard("Stages", String(problem.stage_count), problem.available_stages.join(", ") || "no stages")}
            ${infoCard("Expected Answer", problem.problem && problem.problem.answer ? String(problem.problem.answer) : "n/a")}
            ${infoCard("Generation Count", String(problem.generation_count))}
          </div>
          ${problem.problem && problem.problem.statement ? `<div style="margin-top: 16px;"><p class="metric-label">Statement</p><pre>${escapeHtml(problem.problem.statement)}</pre></div>` : ""}
          ${problem.problem && problem.problem.starter_code ? `<div style="margin-top: 16px;"><p class="metric-label">Starter Code</p><pre>${escapeHtml(problem.problem.starter_code)}</pre></div>` : ""}
          ${metadata ? `<div style="margin-top: 16px;"><p class="metric-label">Metadata</p><pre>${escapeHtml(JSON.stringify(metadata, null, 2))}</pre></div>` : ""}
          ${(links.artifact_json_uri || links.artifact_md_uri) ? `
            <div class="note">
              ${(links.artifact_json_uri ? `<a href="${escapeHtml(links.artifact_json_uri)}" target="_blank" rel="noreferrer">Open artifact.json</a>` : "")}
              ${(links.artifact_json_uri && links.artifact_md_uri) ? " · " : ""}
              ${(links.artifact_md_uri ? `<a href="${escapeHtml(links.artifact_md_uri)}" target="_blank" rel="noreferrer">Open artifact.md</a>` : "")}
            </div>
          ` : ""}
        </section>
      `;
    }

    function renderGeneration(problem) {
      const generation = problem && problem.stages ? problem.stages.generation : null;
      if (!generation) {
        return `<section class="panel"><div class="empty">No generation data for this problem.</div></section>`;
      }
      return `
        ${renderPromptPanel("Generation", generation)}
        <section class="panel">
          <h2>Solutions</h2>
          <p class="section-subtitle">${generation.solutions ? generation.solutions.length : 0} sampled generations.</p>
          ${renderSolutionCards("Generation", generation.solutions || [], (problem.stages.scoring && problem.stages.scoring.scores) || [])}
        </section>
      `;
    }

    function renderScoring(problem) {
      const scoring = problem && problem.stages ? problem.stages.scoring : null;
      if (!scoring) {
        return `<section class="panel"><div class="empty">No scoring data for this problem.</div></section>`;
      }
      const scoreSummary = problem.score_summary || {};
      return `
        <section class="panel">
          <h2 class="section-title">Scoring</h2>
          <div class="kv-grid" style="margin-top: 14px;">
            ${infoCard("Scored Outputs", String(scoreSummary.count || 0))}
            ${infoCard("Mean Score", scoreSummary.mean_score === null || scoreSummary.mean_score === undefined ? "n/a" : Number(scoreSummary.mean_score).toFixed(3))}
            ${infoCard("Top Tier", scoreSummary.top_tier || "n/a")}
            ${infoCard("Tier Breakdown", scoreSummary.tier_breakdown || "n/a")}
          </div>
          <div style="margin-top: 16px;">
            ${renderScoreTable(scoring.scores || [])}
          </div>
        </section>
        ${(problem.stages.generation && problem.stages.generation.solutions) ? `
          <section class="panel">
            <h2>Scored Generations</h2>
            ${renderSolutionCards("Generation", problem.stages.generation.solutions || [], scoring.scores || [])}
          </section>
        ` : ""}
      `;
    }

    function renderMemory(problem) {
      const memory = problem && problem.stages ? problem.stages.memory : null;
      if (!memory) {
        return `<section class="panel"><div class="empty">No memory data for this problem.</div></section>`;
      }
      const grouped = memory.grouped_solutions || {};
      return `
        <section class="panel">
          <h2 class="section-title">Memory</h2>
          <div class="kv-grid" style="margin-top: 14px;">
            ${infoCard("Skipped", memory.skipped ? "true" : "false", memory.skip_reason || "")}
            ${infoCard("Memory Items", String((memory.items || []).length))}
          </div>
          ${memory.prompt ? `<div style="margin-top: 16px;"><p class="metric-label">Prompt</p><pre>${escapeHtml(memory.prompt)}</pre></div>` : ""}
          ${(memory.items || []).length ? `
            <div style="margin-top: 16px;">
              <p class="metric-label">Parsed Memory Items</p>
              <ol class="list-clean">
                ${(memory.items || []).map((item) => `
                  <li>
                    <strong>${escapeHtml(item.title || item.insight || "")}</strong>
                    ${(item.description || item.insight) ? `<div style="margin-top: 6px;">${escapeHtml(item.description || item.insight || "")}</div>` : ""}
                    ${item.content && item.content !== item.description ? `<div class="muted" style="margin-top: 6px;">${escapeHtml(item.content)}</div>` : ""}
                    ${item.reasoning ? `<div class="muted" style="margin-top: 6px;">${escapeHtml(item.reasoning)}</div>` : ""}
                  </li>
                `).join("")}
              </ol>
            </div>
          ` : `<div class="empty" style="margin-top: 16px;">No parsed memory items were stored for this problem.</div>`}
          ${memory.raw_response ? `<div style="margin-top: 16px;"><p class="metric-label">Raw Memory Response</p><pre>${escapeHtml(memory.raw_response)}</pre></div>` : ""}
        </section>

        <section class="panel">
          <h2>Grouped Solutions</h2>
          ${Object.keys(grouped).length ? `
            <div class="stack" style="margin-top: 14px;">
              ${Object.entries(grouped).map(([tier, solutions]) => `
                <div>
                  <p class="metric-label">${escapeHtml(tier)}</p>
                  ${renderSolutionCards(`${tier} attempt`, Array.isArray(solutions) ? solutions : [])}
                </div>
              `).join("")}
            </div>
          ` : `<div class="empty" style="margin-top: 14px;">No grouped solutions stored for this problem.</div>`}
        </section>
      `;
    }

    function renderEvaluation(problem) {
      const evaluation = problem && problem.stages ? problem.stages.evaluation : null;
      if (!evaluation) {
        return `<section class="panel"><div class="empty">No evaluation data for this problem.</div></section>`;
      }
      return `
        <section class="panel">
          <h2 class="section-title">Evaluation</h2>
          <div class="three-col" style="margin-top: 14px;">
            ${infoCard("Baseline avg@k", formatRate(evaluation.baseline_pass_rate))}
            ${infoCard("Augmented avg@k", formatRate(evaluation.augmented_pass_rate))}
            ${infoCard("Improvement", formatDelta(evaluation.improvement), evaluation.used_baseline_for_augmented ? "augmented reused baseline outputs" : "")}
          </div>
        </section>

        ${renderPromptPanel("Baseline", evaluation.baseline_prompt)}
        <section class="panel">
          <h2>Baseline Outputs</h2>
          ${renderSolutionCards("Baseline", evaluation.baseline_solutions || [], evaluation.baseline_results || [])}
        </section>

        ${(evaluation.augmented_prompt || (evaluation.augmented_solutions || []).length || (evaluation.augmented_results || []).length) ? `
          ${renderPromptPanel("Augmented", evaluation.augmented_prompt)}
          <section class="panel">
            <h2>Augmented Outputs</h2>
            ${renderSolutionCards("Augmented", evaluation.augmented_solutions || [], evaluation.augmented_results || [])}
          </section>
        ` : ""}
      `;
    }

    function renderContent(problem, items) {
      if (state.activeView === "overview") {
        return renderOverview(items);
      }
      if (state.activeView === "problem") {
        return renderProblem(problem);
      }
      if (state.activeView === "generation") {
        return renderGeneration(problem);
      }
      if (state.activeView === "scoring") {
        return renderScoring(problem);
      }
      if (state.activeView === "memory") {
        return renderMemory(problem);
      }
      if (state.activeView === "evaluation") {
        return renderEvaluation(problem);
      }
      return `<section class="panel"><div class="empty">Unknown view.</div></section>`;
    }

    function render() {
      const items = filteredProblems();
      const problem = ensureSelection(items);
      renderSummary();
      renderProblemList(items, problem);
      renderTabs(problem);
      document.getElementById("content").innerHTML = renderContent(problem, items);
    }

    render();
  </script>
</body>
</html>
"""
    return template.replace("__TITLE__", str(data.get("title", "Memgen Viewer"))).replace(
        "__DATA_JSON__", payload
    )


def write_visualization(results_path: str | Path, output_path: str | Path | None = None) -> Path:
    root = Path(results_path).expanduser().resolve()
    output = (
        Path(output_path).expanduser().resolve()
        if output_path is not None
        else root / HTML_FILENAME
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        render_visualization_html(build_visualization_data(root)),
        encoding="utf-8",
    )
    return output


def build_guru_domain_plot_data(results_path: str | Path) -> dict[str, Any]:
    root = Path(results_path).expanduser().resolve()
    evaluation_records = _load_recursive_latest_evaluations(root)
    if not evaluation_records:
        raise ValueError(f"No evaluation records found under {root}")

    domain_index = _load_recursive_domain_index(root)
    rows: list[dict[str, Any]] = []
    unknown_count = 0
    completed_count = len(evaluation_records)

    for domain in DOMAIN_ORDER:
        rows.append(
            {
                "domain": domain,
                "label": DOMAIN_LABELS[domain],
                "count": 0,
                "baseline_sum": 0.0,
                "augmented_sum": 0.0,
                "improvement_sum": 0.0,
                "helped": 0,
                "hurt": 0,
                "unchanged": 0,
            }
        )
    row_by_domain = {row["domain"]: row for row in rows}

    for problem_id, record in evaluation_records.items():
        domain = domain_index.get(problem_id) or _infer_guru_problem_domain(problem_id)
        if domain not in row_by_domain:
            unknown_count += 1
            continue

        baseline = float(record.get("baseline_pass_rate", 0.0) or 0.0)
        augmented = float(record.get("augmented_pass_rate", 0.0) or 0.0)
        improvement = float(record.get("improvement", augmented - baseline) or 0.0)
        row = row_by_domain[domain]
        row["count"] += 1
        row["baseline_sum"] += baseline
        row["augmented_sum"] += augmented
        row["improvement_sum"] += improvement
        if improvement > 0:
            row["helped"] += 1
        elif improvement < 0:
            row["hurt"] += 1
        else:
            row["unchanged"] += 1

    plotted_count = 0
    total_baseline = 0.0
    total_augmented = 0.0
    total_improvement = 0.0
    total_helped = 0
    total_hurt = 0
    total_unchanged = 0
    finalized_rows = []
    for row in rows:
        count = row["count"]
        plotted_count += count
        total_baseline += row["baseline_sum"]
        total_augmented += row["augmented_sum"]
        total_improvement += row["improvement_sum"]
        total_helped += row["helped"]
        total_hurt += row["hurt"]
        total_unchanged += row["unchanged"]
        finalized_rows.append(
            {
                "domain": row["domain"],
                "label": row["label"],
                "count": count,
                "baseline": row["baseline_sum"] / count if count else 0.0,
                "augmented": row["augmented_sum"] / count if count else 0.0,
                "improvement": row["improvement_sum"] / count if count else 0.0,
                "helped": row["helped"],
                "hurt": row["hurt"],
                "unchanged": row["unchanged"],
            }
        )

    return {
        "results_path": str(root),
        "completed_count": completed_count,
        "plotted_count": plotted_count,
        "unknown_count": unknown_count,
        "rows": finalized_rows,
        "summary": {
            "mean_baseline": total_baseline / plotted_count if plotted_count else 0.0,
            "mean_augmented": total_augmented / plotted_count if plotted_count else 0.0,
            "mean_improvement": total_improvement / plotted_count if plotted_count else 0.0,
            "helped": total_helped,
            "hurt": total_hurt,
            "unchanged": total_unchanged,
        },
    }


def write_guru_domain_plots(
    results_path: str | Path,
    output_dir: str | Path | None = None,
) -> dict[str, Path]:
    root = Path(results_path).expanduser().resolve()
    output_root = (
        Path(output_dir).expanduser().resolve()
        if output_dir is not None
        else root / "plots" / "domain_summary"
    )
    output_root.mkdir(parents=True, exist_ok=True)

    data = build_guru_domain_plot_data(root)
    chart_paths = {
        "counts": output_root / DOMAIN_PLOT_FILES["counts"],
        "rates": output_root / DOMAIN_PLOT_FILES["rates"],
        "improvement": output_root / DOMAIN_PLOT_FILES["improvement"],
    }
    chart_paths["counts"].write_text(_render_domain_counts_svg(data), encoding="utf-8")
    chart_paths["rates"].write_text(_render_domain_pass_rates_svg(data), encoding="utf-8")
    chart_paths["improvement"].write_text(_render_domain_improvement_svg(data), encoding="utf-8")

    html_path = output_root / DOMAIN_PLOTS_HTML_FILENAME
    html_path.write_text(
        _render_guru_domain_plots_html(data, chart_paths),
        encoding="utf-8",
    )
    chart_paths["html"] = html_path
    return chart_paths


def _load_stage_records(root: Path, subdir: str, filename: str) -> dict[str, dict[str, Any]]:
    filepath = root / subdir / filename
    if not filepath.exists():
        return {}

    records: dict[str, dict[str, Any]] = {}
    for line in filepath.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        record = json.loads(line)
        problem_id = record.get("problem_id")
        if problem_id:
            records[problem_id] = {k: v for k, v in record.items() if k != "problem_id"}
    return records


def _load_artifacts(root: Path) -> dict[str, dict[str, Any]]:
    artifacts: dict[str, dict[str, Any]] = {}
    for artifact_path in sorted(root.glob("artifacts/*/artifact.json")):
        data = json.loads(artifact_path.read_text(encoding="utf-8"))
        problem_id = data.get("problem_id")
        if not problem_id:
            continue
        artifacts[problem_id] = {"data": data, "path": artifact_path}
    return artifacts


def _load_artifact_index(root: Path) -> dict[str, dict[str, Any]]:
    index_path = root / "artifacts" / "index.json"
    if not index_path.exists():
        return {}

    index = json.loads(index_path.read_text(encoding="utf-8"))
    result: dict[str, dict[str, Any]] = {}
    for record in index:
        problem_id = record.get("problem_id")
        if problem_id:
            result[problem_id] = record
    return result


def _load_recursive_latest_evaluations(root: Path) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for path in _iter_result_files(root, "evaluations", "evaluations.jsonl"):
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            problem_id = record.get("problem_id")
            if not problem_id:
                continue
            result[problem_id] = {k: v for k, v in record.items() if k != "problem_id"}
    return result


def _load_recursive_domain_index(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for index_path in _iter_result_files(root, "artifacts", "index.json"):
        for record in json.loads(index_path.read_text(encoding="utf-8")):
            problem_id = record.get("problem_id")
            domain = record.get("domain")
            if problem_id and domain:
                result[str(problem_id)] = str(domain)
    return result


def _iter_result_files(root: Path, subdir: str, filename: str) -> list[Path]:
    candidates: set[Path] = set()
    direct = root / subdir / filename
    if direct.exists():
        candidates.add(direct)

    for pattern in (
        f"shard_*_of_*/{subdir}/{filename}",
        f"*/shard_*_of_*/{subdir}/{filename}",
    ):
        candidates.update(root.glob(pattern))

    return sorted(path.resolve() for path in candidates if path.exists())


def _build_links(artifact_json_path: Path) -> dict[str, str]:
    artifact_md_path = artifact_json_path.with_name("artifact.md")
    links = {
        "artifact_json_path": str(artifact_json_path),
        "artifact_json_uri": artifact_json_path.resolve().as_uri(),
    }
    if artifact_md_path.exists():
        links["artifact_md_path"] = str(artifact_md_path)
        links["artifact_md_uri"] = artifact_md_path.resolve().as_uri()
    return links


def _build_summary(problems: list[dict[str, Any]]) -> dict[str, Any]:
    stage_counts = {
        stage: sum(1 for problem in problems if stage in problem["available_stages"])
        for stage in STAGE_ORDER
    }
    evaluations = [
        problem
        for problem in problems
        if problem.get("improvement") is not None
        and problem.get("baseline_pass_rate") is not None
        and problem.get("augmented_pass_rate") is not None
    ]

    helped_count = sum(1 for problem in evaluations if problem["improvement"] > 0)
    hurt_count = sum(1 for problem in evaluations if problem["improvement"] < 0)
    no_change_count = sum(1 for problem in evaluations if problem["improvement"] == 0)

    return {
        "stage_counts": stage_counts,
        "evaluation_count": len(evaluations),
        "mean_baseline_pass_rate": _mean(
            [problem["baseline_pass_rate"] for problem in evaluations]
        ),
        "mean_augmented_pass_rate": _mean(
            [problem["augmented_pass_rate"] for problem in evaluations]
        ),
        "mean_improvement": _mean([problem["improvement"] for problem in evaluations]),
        "helped_count": helped_count,
        "hurt_count": hurt_count,
        "no_change_count": no_change_count,
    }


def _summarize_scores(scores: list[dict[str, Any]]) -> dict[str, Any]:
    if not scores:
        return {
            "count": 0,
            "mean_score": None,
            "top_tier": None,
            "tier_breakdown": None,
        }

    tiers = Counter(str(score.get("tier", "")) for score in scores if score.get("tier"))
    mean_score = _mean([float(score.get("score", 0.0)) for score in scores])
    return {
        "count": len(scores),
        "mean_score": mean_score,
        "top_tier": tiers.most_common(1)[0][0] if tiers else None,
        "tier_breakdown": ", ".join(
            f"{tier}: {count}" for tier, count in sorted(tiers.items())
        )
        or None,
    }


def _mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def _infer_guru_problem_domain(problem_id: str) -> str:
    pid = str(problem_id)
    if pid.startswith("codegen__"):
        return "coding"
    if pid.startswith("math__"):
        return "math"
    if pid.startswith("table__"):
        return "table"
    if pid.startswith("stem__") or pid.startswith("stem_"):
        return "science"
    if pid.startswith("simulation__codeio"):
        return "simulation"
    if pid.startswith("logic__"):
        return "logic"
    if pid.startswith(("simulation__arcagi", "simulation__barc")):
        return "logic"
    return "unknown"


def _display_name(root: Path) -> str:
    parts = root.parts
    if "results" in parts:
        index = parts.index("results")
        return "/".join(parts[index + 1 :]) or root.name
    return root.name


def _infer_domain(root: Path) -> str:
    lowered = root.name.lower()
    if lowered in {"math", "coding", "science", "logic", "simulation", "table", "guru"}:
        return lowered
    for path in root.parents:
        lowered = path.name.lower()
        if lowered in {"math", "coding", "science", "logic", "simulation", "table", "guru"}:
            return lowered
    return "unknown"


def _natural_sort_key(value: str) -> list[Any]:
    return [int(chunk) if chunk.isdigit() else chunk.lower() for chunk in re.split(r"(\d+)", value)]


def _render_domain_counts_svg(data: dict[str, Any]) -> str:
    rows = data["rows"]
    width = 980
    left = 190
    right = 80
    top = 70
    row_height = 48
    bottom = 36
    plot_width = width - left - right
    height = top + bottom + row_height * len(rows)
    max_count = max((row["count"] for row in rows), default=1) or 1

    parts = [_svg_header(width, height, "Completed problems by domain")]
    parts.append(f'<text x="{left}" y="36" class="title">Completed Problems By Domain</text>')
    parts.append(f'<text x="{left}" y="56" class="subtitle">Completed subset only</text>')
    for index, row in enumerate(rows):
        y = top + index * row_height
        bar_width = 0 if max_count == 0 else plot_width * row["count"] / max_count
        parts.append(f'<text x="{left - 14}" y="{y + 22}" class="label" text-anchor="end">{html.escape(row["label"])}</text>')
        parts.append(f'<rect x="{left}" y="{y + 8}" width="{plot_width}" height="20" class="bar-track" rx="10"></rect>')
        parts.append(f'<rect x="{left}" y="{y + 8}" width="{bar_width:.2f}" height="20" class="bar-count" rx="10"></rect>')
        parts.append(f'<text x="{left + bar_width + 8:.2f}" y="{y + 22}" class="value">{row["count"]:,}</text>')
    parts.append("</svg>")
    return "".join(parts)


def _render_domain_pass_rates_svg(data: dict[str, Any]) -> str:
    rows = data["rows"]
    width = 980
    left = 190
    right = 90
    top = 82
    row_height = 56
    bottom = 40
    plot_width = width - left - right
    height = top + bottom + row_height * len(rows)

    parts = [_svg_header(width, height, "Baseline vs augmented avg@16 by domain")]
    parts.append(f'<text x="{left}" y="36" class="title">Baseline Vs Augmented Avg@16</text>')
    parts.append(f'<text x="{left}" y="56" class="subtitle">Mean pass rate on completed problems</text>')
    parts.append(f'<rect x="{left}" y="18" width="14" height="14" class="bar-baseline" rx="4"></rect>')
    parts.append(f'<text x="{left + 20}" y="30" class="legend">Baseline</text>')
    parts.append(f'<rect x="{left + 96}" y="18" width="14" height="14" class="bar-augmented" rx="4"></rect>')
    parts.append(f'<text x="{left + 116}" y="30" class="legend">Augmented</text>')
    for index, row in enumerate(rows):
        y = top + index * row_height
        baseline_width = plot_width * row["baseline"]
        augmented_width = plot_width * row["augmented"]
        parts.append(f'<text x="{left - 14}" y="{y + 24}" class="label" text-anchor="end">{html.escape(row["label"])}</text>')
        parts.append(f'<rect x="{left}" y="{y + 6}" width="{plot_width}" height="14" class="bar-track" rx="7"></rect>')
        parts.append(f'<rect x="{left}" y="{y + 30}" width="{plot_width}" height="14" class="bar-track" rx="7"></rect>')
        parts.append(f'<rect x="{left}" y="{y + 6}" width="{baseline_width:.2f}" height="14" class="bar-baseline" rx="7"></rect>')
        parts.append(f'<rect x="{left}" y="{y + 30}" width="{augmented_width:.2f}" height="14" class="bar-augmented" rx="7"></rect>')
        parts.append(f'<text x="{left + baseline_width + 8:.2f}" y="{y + 18}" class="value">{row["baseline"]:.3f}</text>')
        parts.append(f'<text x="{left + augmented_width + 8:.2f}" y="{y + 42}" class="value">{row["augmented"]:.3f}</text>')
    parts.append("</svg>")
    return "".join(parts)


def _render_domain_improvement_svg(data: dict[str, Any]) -> str:
    rows = data["rows"]
    width = 980
    left = 190
    right = 90
    top = 70
    row_height = 48
    bottom = 44
    plot_width = width - left - right
    height = top + bottom + row_height * len(rows)
    max_abs = max((abs(row["improvement"]) for row in rows), default=0.01)
    max_abs = max(max_abs, 0.01)
    zero_x = left + plot_width / 2

    parts = [_svg_header(width, height, "Improvement by domain")]
    parts.append(f'<text x="{left}" y="36" class="title">Mean Improvement By Domain</text>')
    parts.append(f'<text x="{left}" y="56" class="subtitle">Augmented minus baseline avg@16</text>')
    parts.append(f'<line x1="{zero_x:.2f}" y1="{top - 6}" x2="{zero_x:.2f}" y2="{height - bottom + 8}" class="axis-line"></line>')
    parts.append(f'<text x="{left}" y="{height - 12}" class="axis-label" text-anchor="start">-{max_abs:.3f}</text>')
    parts.append(f'<text x="{zero_x:.2f}" y="{height - 12}" class="axis-label" text-anchor="middle">0</text>')
    parts.append(f'<text x="{left + plot_width}" y="{height - 12}" class="axis-label" text-anchor="end">+{max_abs:.3f}</text>')
    for index, row in enumerate(rows):
        y = top + index * row_height
        value = row["improvement"]
        bar_width = (abs(value) / max_abs) * (plot_width / 2)
        bar_x = zero_x if value >= 0 else zero_x - bar_width
        klass = "bar-positive" if value >= 0 else "bar-negative"
        label_x = zero_x + bar_width + 8 if value >= 0 else zero_x - bar_width - 8
        anchor = "start" if value >= 0 else "end"
        parts.append(f'<text x="{left - 14}" y="{y + 22}" class="label" text-anchor="end">{html.escape(row["label"])}</text>')
        parts.append(f'<rect x="{left}" y="{y + 8}" width="{plot_width}" height="20" class="bar-track" rx="10"></rect>')
        parts.append(f'<rect x="{bar_x:.2f}" y="{y + 8}" width="{bar_width:.2f}" height="20" class="{klass}" rx="10"></rect>')
        parts.append(f'<text x="{label_x:.2f}" y="{y + 22}" class="value" text-anchor="{anchor}">{value:+.3f}</text>')
    parts.append("</svg>")
    return "".join(parts)


def _render_guru_domain_plots_html(data: dict[str, Any], chart_paths: dict[str, Path]) -> str:
    summary = data["summary"]
    rows_html = "".join(
        (
            "<tr>"
            f"<td>{html.escape(row['label'])}</td>"
            f"<td>{row['count']:,}</td>"
            f"<td>{row['baseline']:.4f}</td>"
            f"<td>{row['augmented']:.4f}</td>"
            f"<td>{row['improvement']:+.4f}</td>"
            f"<td>{row['helped']}</td>"
            f"<td>{row['hurt']}</td>"
            f"<td>{row['unchanged']}</td>"
            "</tr>"
        )
        for row in data["rows"]
    )
    note = (
        f"<p class='note'>{data['unknown_count']} completed problems fell outside the six-domain plot mapping and were excluded.</p>"
        if data["unknown_count"]
        else ""
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Guru Domain Performance</title>
  <style>
    :root {{
      --bg: #f7f4ec;
      --paper: #fffdf8;
      --ink: #1f2430;
      --muted: #5e6573;
      --line: rgba(48, 58, 79, 0.16);
      --accent: #0f766e;
      --accent-soft: rgba(15, 118, 110, 0.10);
      --good: #18794e;
      --good-soft: rgba(24, 121, 78, 0.14);
      --bad: #b42318;
      --bad-soft: rgba(180, 35, 24, 0.12);
      --warm: #b45309;
      --shadow: 0 18px 40px rgba(31, 36, 48, 0.08);
      --mono: "IBM Plex Mono", "SFMono-Regular", "Menlo", monospace;
      --sans: "Avenir Next", "Segoe UI", "Helvetica Neue", sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 32px;
      color: var(--ink);
      font-family: var(--sans);
      background:
        radial-gradient(circle at top left, rgba(15, 118, 110, 0.14), transparent 24%),
        radial-gradient(circle at bottom right, rgba(180, 83, 9, 0.10), transparent 22%),
        linear-gradient(180deg, #faf6ee 0%, #f0e7d7 100%);
    }}
    .page {{ max-width: 1180px; margin: 0 auto; }}
    h1 {{ margin: 0 0 8px; font-size: 34px; letter-spacing: -0.03em; }}
    .eyebrow {{
      margin: 0 0 6px;
      font-size: 12px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--muted);
    }}
    .subtle {{ color: var(--muted); margin: 0; }}
    .cards {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 14px;
      margin: 22px 0 20px;
    }}
    .card, .panel {{
      background: rgba(255, 255, 255, 0.82);
      border: 1px solid var(--line);
      border-radius: 18px;
      box-shadow: var(--shadow);
      backdrop-filter: blur(16px);
    }}
    .card {{ padding: 16px 18px; }}
    .card .label {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
    }}
    .card .value {{ margin-top: 8px; font-size: 28px; font-weight: 700; }}
    .panel {{ padding: 18px; margin-top: 16px; }}
    .panel h2 {{ margin: 0 0 12px; font-size: 20px; letter-spacing: -0.02em; }}
    .panel img {{
      width: 100%;
      border-radius: 14px;
      border: 1px solid var(--line);
      background: var(--paper);
    }}
    .note {{ margin: 16px 0 0; color: var(--muted); }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
    }}
    th, td {{
      padding: 12px 10px;
      border-top: 1px solid var(--line);
      text-align: left;
    }}
    th {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
    }}
    td:nth-child(n + 2) {{
      font-family: var(--mono);
    }}
    @media (max-width: 960px) {{
      body {{ padding: 18px; }}
      .cards {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    }}
    @media (max-width: 640px) {{
      .cards {{ grid-template-columns: 1fr; }}
      table {{ font-size: 12px; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <p class="eyebrow">Memgen Guru Summary</p>
    <h1>Completed-Domain Performance</h1>
    <p class="subtle">{html.escape(data['results_path'])}</p>
    <div class="cards">
      <div class="card"><div class="label">Completed Problems</div><div class="value">{data['completed_count']:,}</div></div>
      <div class="card"><div class="label">Mean Baseline</div><div class="value">{summary['mean_baseline']:.4f}</div></div>
      <div class="card"><div class="label">Mean Augmented</div><div class="value">{summary['mean_augmented']:.4f}</div></div>
      <div class="card"><div class="label">Mean Improvement</div><div class="value">{summary['mean_improvement']:+.4f}</div></div>
    </div>
    <div class="cards">
      <div class="card"><div class="label">Helped</div><div class="value">{summary['helped']:,}</div></div>
      <div class="card"><div class="label">Hurt</div><div class="value">{summary['hurt']:,}</div></div>
      <div class="card"><div class="label">Unchanged</div><div class="value">{summary['unchanged']:,}</div></div>
      <div class="card"><div class="label">Plotted Domains</div><div class="value">{data['plotted_count']:,}</div></div>
    </div>
    <div class="panel">
      <h2>Completed Count</h2>
      <img src="{chart_paths['counts'].name}" alt="Completed problem counts by domain">
    </div>
    <div class="panel">
      <h2>Baseline Vs Augmented</h2>
      <img src="{chart_paths['rates'].name}" alt="Baseline and augmented pass rates by domain">
    </div>
    <div class="panel">
      <h2>Improvement</h2>
      <img src="{chart_paths['improvement'].name}" alt="Improvement by domain">
    </div>
    <div class="panel">
      <h2>Domain Table</h2>
      <table>
        <thead>
          <tr>
            <th>Domain</th>
            <th>Completed</th>
            <th>Baseline</th>
            <th>Augmented</th>
            <th>Improvement</th>
            <th>Helped</th>
            <th>Hurt</th>
            <th>Unchanged</th>
          </tr>
        </thead>
        <tbody>{rows_html}</tbody>
      </table>
      {note}
    </div>
  </div>
</body>
</html>
"""


def _svg_header(width: int, height: int, title: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(title)}">'
        "<style>"
        ".title{font:700 24px 'Avenir Next','Segoe UI',sans-serif;fill:#1f2430;letter-spacing:-0.03em;}"
        ".subtitle{font:13px 'Avenir Next','Segoe UI',sans-serif;fill:#5e6573;}"
        ".label{font:600 14px 'Avenir Next','Segoe UI',sans-serif;fill:#1f2430;}"
        ".legend,.value,.axis-label{font:12px 'IBM Plex Mono','SFMono-Regular',monospace;fill:#1f2430;}"
        ".bar-track{fill:rgba(48,58,79,0.08);}"
        ".bar-count{fill:#b45309;}"
        ".bar-baseline{fill:#0f766e;}"
        ".bar-augmented{fill:#18794e;}"
        ".bar-positive{fill:#18794e;}"
        ".bar-negative{fill:#b42318;}"
        ".axis-line{stroke:rgba(48,58,79,0.28);stroke-width:1.5;}"
        "</style>"
    )
