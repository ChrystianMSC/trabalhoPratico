
import '@testing-library/jest-dom'
import { TextEncoder } from 'node:util'
global.TextEncoder = TextEncoder
import "jest-canvas-mock";
import { render } from "@testing-library/react"
import App from "../App"
import { Provider } from 'react-redux';
import store from '../redux/store';

jest.mock('axios');
import axios from 'axios';

jest.mock('three', () => {
    const originalModule = jest.requireActual('three');
    return {
      ...originalModule,
      WebGLRenderer: jest.fn().mockImplementation(() => ({
        render: jest.fn(),
        setSize: jest.fn(),
        dispose: jest.fn(),
        setPixelRatio: jest.fn(),
      })),
    };
});


test('demo', () => {
    expect(true).toBe(true)
})

test("Fetches colors on component mount", async () => {
    const mockData = [{ id: 1, color: "#ff0000" }, { id: 2, color: "#00ff00" }];
    (axios.get as jest.Mock).mockResolvedValue({ data: mockData });

    const { findByText } = render(
        <Provider store={store}>
            <App />
        </Provider>
    );

    expect(axios.get as jest.Mock).toHaveBeenCalledWith('http://127.0.0.1:8000/api/colors/');
    await findByText('#ff0000');
    await findByText('#00ff00');
});


test("Renders the main page", async () => {
    render(<Provider store={store}>
       <App />
     </Provider>)
   expect(true).toBeTruthy()
})
