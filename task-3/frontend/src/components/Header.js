import React, {useContext} from "react"

import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import { useNavigate } from "react-router-dom";
import AuthContext from "../context/AuthContext";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

export const Header = () => {
    const classes = useStyles();

    const {logoutUser, user} = useContext(AuthContext)
    const nav = useNavigate()

    const onDataClick = () => {
        nav("/data")
    }

    const onKeysClick = () => {
        nav("/updateUserData")
    }

    const onLogoutClick = () => {
        logoutUser()
    }


    if (!user) {
        return (
            <div>
                
            </div>
        )
    }

    return (
        <div className={classes.root}>
        <AppBar position="static">
          <Toolbar>
            <Button color="inherit" variant="h6" className={classes.title} onClick={onDataClick}>
              Data
            </Button>
            <Button color="inherit" variant="h6" className={classes.title} onClick={onKeysClick}>
              Keys
            </Button>
            <Button color="inherit" onClick={onLogoutClick}> Logout </Button>
          </Toolbar>
        </AppBar>
      </div>
    )
}