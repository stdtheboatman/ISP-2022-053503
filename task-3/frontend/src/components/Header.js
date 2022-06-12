import React, { useContext } from 'react'
import { Link } from 'react-router-dom' 
import AuthContext from '../context/AuthContext'

export const Header = () => {
    const {user, logoutUser} = useContext(AuthContext)
    
    return (
    <div>
        <Link to="/"> Home </Link>
        {!user ?
            <Link to="/login"> Login </Link> :
            <Link to="/login" onClick={logoutUser}> Logout</Link>
        }
        <Link to="/updateUserData"> Update Data </Link>
        <Link to="/data"> Data </Link>
        
    </div>
    )
}
