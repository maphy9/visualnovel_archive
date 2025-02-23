import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import App from './Components/App/App';
import Home from './Components/Home/Home';
import './style.css'
import NotFound from './Components/NotFound/NotFound';
import About from './Components/Informational/About'
import PrivacyPolicy from './Components/Informational/PrivacyPolicy'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={ <App /> }>
        <Route index element={ <Home /> } />
        <Route path="about" element={ <About /> } />
        <Route path="privacy_policy" element={ <PrivacyPolicy /> } />
        <Route path="*" element={ <NotFound /> } />
      </Route>
    </Routes>
  </BrowserRouter>
);
