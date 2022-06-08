import React from 'react';
import './App.css';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import {HomePage} from './pages/HomePage';
import {LoginPage} from './pages/LoginPage';

import {Header} from './components/Header';
import {PrivateRoute} from './utils/PrivateRoute';

import {AuthProvider} from "./context/AuthContext"
import {UpdateUserDataPage} from './pages/UpdateUserDataPage';

function App() {
  return (
      <div className="App">
        <Router>
          <AuthProvider>
            <Header />
            <Routes>
              <Route element={<LoginPage />} path="/login" />

    
              <Route element={<PrivateRoute> <HomePage/> </PrivateRoute>} path="/" exact />
              <Route element={<PrivateRoute> <UpdateUserDataPage/> </PrivateRoute>} path="/updateUserData" exact />

          

            </Routes>
          </AuthProvider>
        </Router>
      </div>
  );
}

export default App;
