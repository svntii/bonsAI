module.exports = {
  presets: ['module:@react-native/babel-preset'],
  plugins: [
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
          '@assets': './src/assets',
          '@features': './src/features',
          '@providers': './src/providers',
          '@screens': './src/screens',
          '@theme': './src/theme',
          '@utils': './src/utils',
        },
      },
    ],
  ],
};
