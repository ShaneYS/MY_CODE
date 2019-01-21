def img2vector(filename):
    # ��������
    returnVect = np.zeros((1, 1024))
    # �������ļ�����ȡÿ������
    fr = open(filename)
    for i in range(32):
        # ��ȡÿһ��
        lineStr = fr.readline()
        # ��ÿ��ǰ 32 �ַ�ת�� int ��������
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])

    return returnVect
    
# img2vector('digits/testDigits/0_1.txt')




import operator


def classify0(inX, dataSet, labels, k):

    """
    ����:
    - inX: ���ڷ������������
    - dataSet: �����ѵ��������
    - labels: �������ݵ����ǩ����
    - k: ����ѡ������ھӵ���Ŀ
    """

    # ��ȡ������������
    dataSetSize = dataSet.shape[0]

    # �������㣬�������������ÿ���������ݶ�Ӧ������Ĳ�ֵ
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet

    # sqDistances ��һ������ƽ����
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)

    # ȡƽ�������õ���������
    distances = sqDistances**0.5

    # ���վ���ӵ͵�������
    sortedDistIndicies = distances.argsort()
    classCount = {}

    # ����ȡ���������������
    for i in range(k):
        # ��¼�������������������
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    # �������ֵ�Ƶ�ν������򣬴Ӹߵ���
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True)

    # ���س���Ƶ����ߵ����
    return sortedClassCount[0][0]


# group, labels = createDataSet()
# print(classify0([0, 0], group, labels, 3))



from os import listdir


def handwritingClassTest():
    # �������ݵ����ǩ�б�
    hwLabels = []

    # ���������ļ��б�
    trainingFileList = listdir('digits/trainingDigits')
    m = len(trainingFileList)

    # ��ʼ���������ݾ���M*1024��
    trainingMat = np.zeros((m, 1024))

    # ���ζ�ȡ�����������ݵ����ݾ���
    for i in range(m):
        # ��ȡ�ļ����е�����
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)

        # ���������ݴ������
        trainingMat[i, :] = img2vector(
            'digits/trainingDigits/%s' % fileNameStr)

    # ѭ����ȡ��������
    testFileList = listdir('digits/testDigits')

    # ��ʼ��������
    errorCount = 0.0
    mTest = len(testFileList)

    # ѭ������ÿ�����������ļ�
    for i in range(mTest):
        # ��ȡ�ļ����е�����
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])

        # ��ȡ��������
        vectorUnderTest = img2vector('digits/testDigits/%s' % fileNameStr)

        # �������ļ����з���
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)

        # ��ӡ K �����㷨����������ʵ�ķ���
        print("�������� %d, ������Ԥ��: %d, ��ʵ���: %d" %
              (i+1, classifierResult, classNumStr))

        # �ж�K �����㷨����Ƿ�׼ȷ
        if (classifierResult != classNumStr):
            errorCount += 1.0

    # ��ӡ������
    print("\n����������: %d" % errorCount)
    print("\n����������: %f" % (errorCount/float(mTest)))



print(handwritingClassTest())