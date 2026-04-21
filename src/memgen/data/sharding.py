from __future__ import annotations

import hashlib

from memgen.config import DatasetConfig


def is_problem_in_shard(problem_id: str, config: DatasetConfig | None) -> bool:
    if config is None or not config.is_sharded:
        return True
    return shard_index_for_problem(problem_id, config.num_shards) == config.shard_index


def shard_index_for_problem(problem_id: str, num_shards: int | None) -> int:
    if num_shards in (None, 0):
        return 0
    digest = hashlib.sha1(str(problem_id).encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") % num_shards
