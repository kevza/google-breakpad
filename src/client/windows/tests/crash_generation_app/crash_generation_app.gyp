# Copyright 2010 Google Inc. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

{
  'includes': [
    '../../../../build/common.gypi',
  ],
  'targets': [
    {
      'target_name': 'crash_generation_app',
      'type': 'executable',
      'sources': [
        'abstract_class.cc',
        'abstract_class.h',
        'crash_generation_app.cc',
        'crash_generation_app.h',
        'crash_generation_app.ico',
        'resource.rc',
        'resource.h',
        'small.ico',
      ],
      'dependencies': [
        '../../breakpad_client.gyp:common',
        '../../crash_generation/crash_generation.gyp:crash_generation_server',
        '../../crash_generation/crash_generation.gyp:crash_generation_client',
        '../../handler/exception_handler.gyp:exception_handler',
      ],
      'conditions': [
          [ '"<(GENERATOR)" == "make"', {
              'ldflags': [
                  '-Wl,--subsystem=2', '-municode'
              ],
              'rules': [
                  { 'rule_name': 'windres',
                    'extension': 'rc',
                    'inputs'   : [ ],
                    'outputs'  : [ '$(builddir)/<(RULE_INPUT_ROOT).o' ],
                    'action'   : [ '$(RC)', '--input=<(RULE_INPUT_PATH)', '--output=$(builddir)/<(RULE_INPUT_ROOT).o', '--input-format=rc', '--output-format=coff', '-v', '--use-temp-file' ],
                    'message'  : 'Compiling Windows resources',
                    'process_outputs_as_sources' : 1,
                },
              ],
            }
          ],
          [ '"<(GENERATOR)" == "msvs"', {
              'libraries': [
                  'user32.lib',
              ],
            }
          ]
      ],
      'msvs_settings': {
        'VCLinkerTool': {
          'SubSystem': '2',  # Windows Subsystem as opposed to a console app
        },
      },
    }
  ]
}
