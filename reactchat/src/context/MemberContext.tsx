import React, {createContext, useContext} from 'react';
import useMembershipService from '../services/MembershipService.ts';

interface IUseServer{
    joinServer: (serverId: number) => Promise<void>;
    leaveServer: (serverId: number) => Promise<void>;
    isMember: (serverId: number) => Promise<boolean>;
    isUserMember: boolean;
    error: Error | null;
    isLoading: boolean;
}


const MembershipContext = createContext<IUseServer | null>(null);

export function MembershipProvider(props: React.PropsWithChildren<{}>) {
  const membership = useMembershipService();
  return (
    <MembershipContext.Provider value={membership}>
      {props.children}
    </MembershipContext.Provider>
  );
}

export function useMembershipContext(): IUseServer {
  const context = useContext(MembershipContext);

  if (context === null) {
    throw new Error("Error - You have to use the MembershipProvider");
  }
  return context;
}

export default MembershipProvider;