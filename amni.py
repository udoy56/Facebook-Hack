{

  "name": "Fakebook",

  "version": "0.0.0",

  "description": "A clone of Facebook",

  "main": "index.js",

  "scripts": {

    "test": "echo \"Error: no test specified\" && exit 1"

  },

  "author": "Fakebook Organization",

  "license": "ISC",

  "devDependencies": {

    "babel-core": "^6.3.26",

    "babel-loader": "^6.2.0",

    "babel-plugin-transform-object-rest-spread": "^6.3.13",

    "babel-preset-es2015": "^6.3.13",

    "babel-preset-react": "^6.3.13",

    "css-loader": "^0.23.1",

    "node-sass": "^3.8.0",

    "sass-loader": "^4.0.1",

    "style-loader": "^0.13.1",

    "webpack": "^1.12.9"

  },

  "babel": {

    "presets": [

      "es2015",

      "react"

    ],

    "plugins": [

      "transform-object-rest-spread"

    ]

  },

  "dependencies": {

    "axios": "^0.14.0",

    "react": "^15.0.2",

    "react-dom": "^15.0.2",

    "react-facebook-login": "^3.2.0",

    "react-router": "^2.7.0",

    "react-sticky": "^5.0.5"

  }

}
