import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel11FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel11FlatComponentChunk37

end RHP2Bridge
