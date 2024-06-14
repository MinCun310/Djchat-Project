import {Box, CssBaseline} from "@mui/material";
import PrimaryAppBar from "./templates/PrimaryAppBar";
import PrimaryDraw from "./templates/PrimaryDraw";
import SecondaryDraw from "./templates/SecondaryDraw";
import Main from "./templates/Main";
import MessageInterface from "../components/Main/MessageInterface.tsx";
import ServerChannels from '../components/SecondaryDraw/ServerChannels.tsx';
import UserServers from '../components/PrimaryDraw/UserServers.tsx';
import {useNavigate, useParams} from "react-router-dom";
import useCRUD from "../hooks/useCRUD.ts";
import {Server} from "../@types/server.d";
import {useEffect} from "react";

const Server = () => {

        const navigate = useNavigate();
        const {serverId, channelId} = useParams();

        const {dataCRUD, error, isLoading, fetchData} = useCRUD<Server>(
            [],
            `/djchat/server/?server_id=${serverId}/`
        );

        if (error !== null && error.message === '400') {
            navigate('/');
            return null;
        }


        // const isChannel = (): boolean => {
        //     if (channelId) {
        //         return true;
        //     }
        //     return dataCRUD.some((server) => server.channel_server.some((channel) => channel.id === parseInt(channelId)));
        // };

        return (
            <Box sx={{display: "flex"}}>
                <CssBaseline/>
                <PrimaryAppBar/>
                <PrimaryDraw>
                    <UserServers open={false} data={dataCRUD}/>
                </PrimaryDraw>
                <SecondaryDraw>
                    <ServerChannels/>
                </SecondaryDraw>
                <Main>
                    <MessageInterface/>
                </Main>
            </Box>
        );
    }
;
export default Server;
