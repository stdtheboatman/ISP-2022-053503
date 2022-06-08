import React from "react";
import jwtDecode from "jwt-decode";
import {useNavigate} from "react-router-dom"
import { createContext, useState, useEffect } from "react";

const AuthContext = createContext()

export default AuthContext

export const AuthProvider = ({children}) => {
    const [authTokens, setAuthTokens] = useState(() => localStorage.getItem("authTokens") ? JSON.parse(localStorage.getItem("authTokens")) : null)
    const [user, setUser] = useState(() => localStorage.getItem("authTokens") ? jwtDecode(localStorage.getItem("authTokens")) : null)

    const navigate = useNavigate()

    const loginUser = async (event) => {
        event.preventDefault()

        const response = await fetch("http://127.0.0.1:8000/api/token/", {
            method: "Post",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                'username': event.target.username.value,
                'password': event.target.password.value
            })
        })

        const data = await response.json()
        
        if (response.status == 200) {
            setAuthTokens(data)
            setUser(jwtDecode(data.access))
            localStorage.setItem("authTokens", JSON.stringify(data))
            navigate("/")

        } else {
            alert("Something went wrong")
        }
    }

    const updateUserData = async (event) => {
        event.preventDefault()

        const response = await fetch("http://127.0.0.1:8000/api/setUserData/", {
            method: "Post",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + String(authTokens.access) 
            },
            body: JSON.stringify({
                "apiKey": event.target.apiKey.value,
                "secretKey": event.target.secretKey.value,
            })
        })

        const data = await response.json()
        
        if (response.status === 200) {
        } else {
            alert("Something went wrong with update user data")
        }
    }

    const logoutUser = () => {
        setAuthTokens(null)
        setUser(null)
        localStorage.removeItem('authTokens')
    }

    const updateToken = async () => {
        console.log("update token")
        const response = await fetch("http://127.0.0.1:8000/api/token/refresh/", {
            method: "Post",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                'refresh': authTokens.refresh,
            })
        })

        const data = await response.json()
        if (response.status === 200) {
            const currentData = JSON.parse(localStorage.getItem("authTokens"))
            currentData.access = data.access
            
            setAuthTokens(currentData)
            setUser(jwtDecode(currentData.access))

            localStorage.setItem("authTokens", JSON.stringify(currentData))

        } else {
            alert("Update failed")
            logoutUser()
        }
    }

    const contextData = {
        user: user,
        loginUser: loginUser,
        logoutUser: logoutUser,
        updateUserData: updateUserData
    }

    useEffect(() => {
        const interval = setInterval(() => {
            if (authTokens) {
                updateToken()
            }
        }, 1000 * 5 * 60)

        return () => clearInterval(interval)
    }, [authTokens])

    return (
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    )
}
