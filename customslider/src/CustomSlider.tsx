import React  from 'react';
import {useEffect} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { Streamlit, RenderData, StreamlitComponentBase,
  withStreamlitConnection} from "streamlit-component-lib";



const CustomSlider = () => {
  // This React component returns (and renders) this <h1> block

  useEffect(() => Streamlit.setFrameHeight());

  <React.StrictMode>
    <h1>Continued Work</h1>
  </React.StrictMode>
  return <h1>Hello World 1</h1>;
};

Streamlit.setComponentReady();

export default withStreamlitConnection(CustomSlider);


