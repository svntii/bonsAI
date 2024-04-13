module.exports = {
  presets: ['module:metro-react-native-babel-preset'],
  plugins: [
    'react-native-reanimated/plugin',
    [
      'module-resolver',
      {
        root: ['.'],
        extensions:[
          ".ts",
          ".tsx",
          ".js",
          ".jsx",
          ".json"
        ],
        alias: {
          '@api': './src/api',
          '@features': './src/features',
          '@navigation': './src/navigation',
          '@providers': './src/providers',
          '@screens': './src/screens',
          '@theme': './src/theme',
          '@utils': './src/utils',
        },
      },
    ],
  ],
};