import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel2FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel2FlatComponentChunk30

end RHP2Bridge
