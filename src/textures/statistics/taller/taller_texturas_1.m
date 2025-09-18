%% Análisis de Texturas en MATLAB
% Comparación: GLCM, LBP, Gabor y Wavelets
clc; clear; close all;

% Directorio de imágenes de entrada
inputDir = 'src/img/texturas'; 

% Archivo CSV de salida
outputCSV = 'src/textures/statistics/taller/resultados_texturas_matlab.csv';

% Extensiones válidas
exts = {'.png','.jpg','.jpeg','.tif'};

% Crear directorio de entrada si no existe
if ~exist(inputDir, 'dir')
    mkdir(inputDir);
    warning('El directorio de entrada estaba vacío, se creó: %s', inputDir);
end

% Listar imágenes
files = dir(inputDir);
files = files(~[files.isdir]); % solo archivos

% Inicializar resultados
results = [];

for k = 1:length(files)
    [~, name, ext] = fileparts(files(k).name);
    if ~ismember(lower(ext), exts)
        continue; % saltar archivos que no son imágenes válidas
    end
    
    % Leer imagen
    I = imread(fullfile(inputDir, files(k).name));
    if size(I,3) == 3
        I = rgb2gray(I);
    end
    
    %% 1. GLCM (Haralick Features)
    GLCM = graycomatrix(I,'Offset',[0 1]); 
    stats = graycoprops(GLCM,{'Contrast','Correlation','Energy','Homogeneity'});
    
    %% 2. LBP (Local Binary Patterns)
    lbpFeatures = extractLBPFeatures(I,'CellSize',[32 32]);
    lbpMean = mean(lbpFeatures);
    lbpStd = std(lbpFeatures);
    
    %% 3. Gabor Features
    wavelength = 4;  
    orientation = [0 45 90 135]; 
    gaborArray = gabor(wavelength,orientation);
    gaborMag = imgaborfilt(I,gaborArray);
    
    % Media de cada magnitud
    gaborMeans = zeros(1,length(orientation));
    for i = 1:length(orientation)
        gaborMeans(i) = mean2(gaborMag(:,:,i));
    end
    
    %% 4. Wavelet Transform
    [cA,cH,cV,cD] = dwt2(I,'db1'); 
    waveletEnergy = [sum(cA(:).^2), sum(cH(:).^2), sum(cV(:).^2), sum(cD(:).^2)];
    
    %% Guardar en resultados
    row = table({files(k).name}, ...
        stats.Contrast, stats.Correlation, stats.Energy, stats.Homogeneity, ...
        lbpMean, lbpStd, ...
        gaborMeans(1), gaborMeans(2), gaborMeans(3), gaborMeans(4), ...
        waveletEnergy(1), waveletEnergy(2), waveletEnergy(3), waveletEnergy(4), ...
        'VariableNames', {'Imagen','GLCM_Contraste','GLCM_Correlacion','GLCM_Energia','GLCM_Homogeneidad', ...
                          'LBP_Media','LBP_Desv','Gabor_0','Gabor_45','Gabor_90','Gabor_135', ...
                          'Wavelet_Aprox','Wavelet_Horiz','Wavelet_Vert','Wavelet_Diag'});
    
    results = [results; row];
end

%% Exportar a CSV
% Crear directorio de salida si no existe
outDir = fileparts(outputCSV);
if ~exist(outDir, 'dir')
    mkdir(outDir);
end

writetable(results, outputCSV, 'Delimiter','|'); % usamos "|" en lugar de ","
fprintf('Resultados guardados en %s\n', outputCSV);
