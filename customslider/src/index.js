import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import CustomSlider from "./CustomSlider.tsx";
import SelectableDataTable from "./selectable_data_table.tsx"

import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>

    <SelectableDataTable />
  </React.StrictMode>,

  document.getElementById('root')
);



// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
