const webpack = require('webpack');
const path = require('path');

module.exports = {
  entry: {
    bundle: './src/index.js'
  },
  output: {
    path: path.resolve('app', 'static', 'js', 'app'),
    filename: '[name].js'
  },
  module: {
    rules: [{
      test: /\.jsx?$/,
      loader: 'babel-loader',
      options: {
        presets: [
          'es2015',
          'react',
          'stage-0'
        ],
      },
      exclude: ['/node_modules'],
    }],
  },
  plugins: [],
  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.json', '.jsx', '.css'],
  }
}
