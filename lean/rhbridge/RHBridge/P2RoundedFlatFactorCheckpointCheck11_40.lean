import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel11FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel11FlatComponentChunk40

end RHP2Bridge
