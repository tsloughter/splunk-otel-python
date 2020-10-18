# Copyright 2020 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pkg_resources

pkg = pkg_resources.get_distribution("splunk-opentelemetry")

__version__ = pkg.version


def format_version_info():
    lines = []
    lines.append('splunk-opentelemetry=={0}'.format(pkg.version))
    lines.append('\n\nAlso uses the following OpenTelemetry libraries:\n')
    for dep in pkg.requires():
      if 'opentelemetry' in dep.name:
        lines.append('\t{0}'.format(str(dep)))

    return '\n'.join(lines)
    
    