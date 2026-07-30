import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel11FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel11FlatComponentChunk36

end RHP2Bridge
