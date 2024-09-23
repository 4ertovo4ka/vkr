/*
 * Project: backend
 * File: \webpack.config.js
 * Created at: Thursday, November 14th 2019, 13:36:12 +03:00
 * Author: Tamara A. Repina (4ertovo4ka@gmail.com)
 * -----
 * Last Modified: Friday, September 20th 2024, 01:06:27 +03:00
 * Modified By: Tamara A. Repina (4ertovo4ka@gmail.com>)
 * Last version: <<projectversion>>
 * -----
 * Copyright 2024 Tamara A. Repina
 * License: GNU Affero General Public License v3.0 https://www.gnu.org/licenses/agpl.txt
 */


const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, './webapp/static'),
        filename: 'js/bundle.js'
    },
    module: {
        rules: [{
            test: /\.scss$/,
            use: [
                MiniCssExtractPlugin.loader,
                {
                    loader: 'css-loader'
                },
                {
                    loader: 'sass-loader',
                    options: {
                        sourceMap: true,
                        // options...
                    }
                }
            ]
        }]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'css/style.css'
        }),
    ]
};
