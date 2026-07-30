import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel1FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel1FlatComponentChunk30

end RHP2Bridge
