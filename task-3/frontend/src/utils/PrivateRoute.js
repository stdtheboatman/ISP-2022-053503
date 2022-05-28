import React, { useContext } from 'react'
import { Navigate } from 'react-router-dom'
import AuthContext from '../context/AuthContext'

const PrivateRoute = ({children}) => {
    const {user} = useContext(AuthContext)
    return (
        <div>
            { user ? 
                children : <Navigate to="/login" /> }
        </div>
    )
}

export default PrivateRoute