import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel2FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel2FlatComponentChunk36

end RHP2Bridge
