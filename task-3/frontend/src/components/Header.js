import React, { useContext } from 'react'
import { Link } from 'react-router-dom' 
import AuthContext from '../context/AuthContext'

const Header = () => {
    const {user, logoutUser} = useContext(AuthContext)
    
    return (
    <div>
        <Link to="/"> Home </Link>
        {!user ?
            <Link to="/login"> Login </Link> :
            <Link to="/login" onClick={logoutUser}> Logout</Link>
        }

        { user  && <p> Hello {user.user_id} </p> }
    </div>
    )
}

export default Header