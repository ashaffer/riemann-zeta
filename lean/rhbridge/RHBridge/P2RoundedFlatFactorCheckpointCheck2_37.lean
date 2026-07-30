import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel2FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel2FlatComponentChunk37

end RHP2Bridge
