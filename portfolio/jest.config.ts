import type { Config } from '@jest/types';

const config: Config.InitialOptions = {
  preset: 'ts-jest',
  transform: {
    "^.+\\.(ts|tsx)$": "ts-jest", // Transform TypeScript files
    "^.+\\.js$": "babel-jest", // Transform JS files using Babel
    "^.+\\.css$": "jest-css-modules-transform", // Transform CSS files
  },
  transformIgnorePatterns: [
      "node_modules/(?!three)"
    ],
  moduleNameMapper: {
    '^three$': require.resolve('three'), // Ensure that three is properly resolved
  },
  testEnvironment: "jest-environment-jsdom", // Use jsdom for browser-like environment
};

export default config;
