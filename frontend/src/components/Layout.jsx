import { Box } from '@mui/material';
import Navigation from './Navigation';
import Footer from './Footer';

export default function Layout({ children, isLoggedIn = false, hideFooter = false, showReturnToDashboard = false }) {
  return (
    <Box 
      minHeight="100vh" 
      display="flex" 
      flexDirection="column"
      sx={{
        scrollBehavior: 'smooth',
        // Optimize for mobile scrolling performance
        WebkitOverflowScrolling: 'touch',
        // Prevent horizontal scroll on mobile
        overflowX: 'hidden',
      }}
    >
      <Navigation 
        isLoggedIn={isLoggedIn} 
        showReturnToDashboard={showReturnToDashboard} 
      />
      
      <Box 
        component="main" 
        flexGrow={1}
        sx={{
          // Ensure proper mobile scrolling
          WebkitOverflowScrolling: 'touch',
        }}
      >
        {children}
      </Box>
      
      {!hideFooter && <Footer />}
    </Box>
  );
}
