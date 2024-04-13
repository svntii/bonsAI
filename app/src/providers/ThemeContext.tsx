// ThemeContext.tsx
import React, {createContext, useState, ReactNode} from 'react';

export const ThemeContext = createContext({
  isDarkMode: false,
  toggle: () => {},
});

interface ThemeProviderProps {
  children: ReactNode;
}

export const ThemeProvider: React.FC<ThemeProviderProps> = ({children}) => {
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggle = () => {
    setIsDarkMode(!isDarkMode);
  };

  return (
    <ThemeContext.Provider value={{isDarkMode, toggle}}>
      {children}
    </ThemeContext.Provider>
  );
};
