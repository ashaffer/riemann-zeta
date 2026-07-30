import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel1FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel1FlatComponentChunk38

end RHP2Bridge
