import React, {useContext} from "react"
import AuthContext from "../context/AuthContext"

export const HomePage = () => {
    const {user} = useContext(AuthContext)
    return (
        <div>
            HomePage
        </div>
    )
}