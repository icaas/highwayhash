{
  'target_defaults': {
    'include_dirs': ['src'],
    'cflags_cc': [
      '-fexceptions',
      '-Wall',
      '-O3'
    ],
    'xcode_settings': {
      'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
      'CLANG_CXX_LIBRARY': 'libc++',
      'MACOSX_DEPLOYMENT_TARGET': '10.7',
      'OTHER_CPLUSPLUSFLAGS': [
        '-fexceptions',
        '-Wall',
        '-O3'
      ]
    },
    'msvs_settings': {
      'VCCLCompilerTool': {
        'ExceptionHandling': 1,
        'DisableSpecificWarnings': ['4477']
      }
    }
  },
  'targets': [
    {
      'target_name': 'arch_specific',
      'type': 'static_library',
      'sources': ['src/highwayhash/arch_specific.cc'],
    }, {
      'target_name': 'hh_avx2',
      'dependencies': ['arch_specific'],
      'type': 'static_library',
      'sources': ['src/highwayhash/highwayhash_target.cc'],
      'defines': [
        'HH_TARGET=TargetAVX2',
        'HH_TARGET_AVX2'
      ],
      'cflags_cc': [
        '-mavx2'
      ],
      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS': [
          '-mavx2'
        ]
      }
    }, {
      'target_name': 'hh_sse41',
      'dependencies': ['arch_specific'],
      'type': 'static_library',
      'sources': ['src/highwayhash/highwayhash_target.cc'],
      'defines': [
        'HH_TARGET=TargetSSE41',
        'HH_TARGET_SSE41'
      ],
      'cflags_cc': [
        '-msse4.1'
      ],
      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS': [
          '-msse4.1'
        ]
      }
    }, {
      'target_name': 'hh_portable',
      'dependencies': ['arch_specific'],
      'type': 'static_library',
      'sources': ['src/highwayhash/highwayhash_target.cc'],
      'defines': [
        'HH_TARGET=TargetPortable',
        'HH_TARGET_PORTABLE'
      ]
    }, {
      'target_name': 'instruction_sets',
      'dependencies': ['hh_avx2', 'hh_sse41', 'hh_portable'],
      'type': 'static_library',
      'sources': ['src/highwayhash/instruction_sets.cc'],
      'defines': [
        'HH_TARGET=TargetPortable',
        'HH_TARGET_PORTABLE'
      ]
    }, {
      'target_name': 'highwayhash',
      'dependencies': ['instruction_sets'],
      'sources': ['src/bindings.cc'],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")'
      ],
      'cflags_cc': [
        '-flto'
      ]
    }
  ]
}
