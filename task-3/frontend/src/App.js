import React from 'react';
import './App.css';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';

import Header from './components/Header';
import PrivateRoute from './utils/PrivateRoute';

import {AuthProvider} from "./context/AuthContext"

function App() {
  return (
      <div className="App">
        <Router>
          <AuthProvider>
            <Header />
            <Routes>
              <Route element={<PrivateRoute />} path='/' exact>
                <Route element={<HomePage />} path="/" exact />
              </Route>
              <Route element={<LoginPage />} path="/login" />
            </Routes>
          </AuthProvider>
        </Router>
      </div>
  );
}

export default App;
