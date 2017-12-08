# Copyright 2017 Google Inc. All rights reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import sys
from ftl.common import args
from ftl.benchmark import benchmark

_RUNTIME = "node"

parser = args.base_parser()
node_parser = argparse.ArgumentParser(
    add_help=False,
    parents=[parser], description='Run node benchmark.')

node_parser.add_argument(
    '--iterations',
    action='store',
    type=int,
    default=5,
    help='Number of times to build the image')

node_parser.add_argument(
    '--description',
    action='store',
    help=('Description of the app being benchmarked.'))

node_parser.add_argument(
        '--project',
        action='store',
        default='ftl-node-test',
        help='Bigquery project build times should be stored in')

node_parser.add_argument(
        '--dataset',
        action='store',
        default='ftl_benchmark',
        help='Bigquery dataset build times should be stored in')

node_parser.add_argument(
        '--table',
        action='store',
        default='ftl_benchmark',
        help='Bigquery table build times should be stored in')


def main(args):
    args = node_parser.parse_args(args)
    b = benchmark.Benchmark(args, _RUNTIME)
    b.run_benchmarks()


if __name__ == '__main__':
    main(sys.argv[1:])
