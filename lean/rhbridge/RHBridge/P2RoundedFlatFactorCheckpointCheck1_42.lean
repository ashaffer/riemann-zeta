import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel1FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel1FlatComponentChunk42

end RHP2Bridge
