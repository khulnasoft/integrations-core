# (C) Khulnasoft, Inc. 2010-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

# 3p
import psutil

# project
from khulnasoft_checks.base import AgentCheck


class SystemSwap(AgentCheck):
    def check(self, instance):
        swap_mem = psutil.swap_memory()
        tags = instance.get('tags', [])
        self.rate('system.swap.swapped_in', swap_mem.sin, tags=tags)
        self.rate('system.swap.swapped_out', swap_mem.sout, tags=tags)
