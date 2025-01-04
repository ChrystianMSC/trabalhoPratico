import { useSelector } from 'react-redux';
import './TopBar.css';

function TopBar() {
  const torusColor = useSelector((state: any) => state.app.torusColor);

  return (
    <div className="top-bar">
      <div className="color-block">
        <span
          className="color-box"
          style={{
            backgroundColor: torusColor,
          }}
        />
        <span className="color-text">{torusColor}</span>
      </div>
      <p className="instructions">Click and drag to navigate the torus</p>
    </div>
  );
}

export default TopBar;
