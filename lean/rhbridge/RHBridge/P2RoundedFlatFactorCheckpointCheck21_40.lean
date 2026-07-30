import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel21FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel21FlatComponentChunk40

end RHP2Bridge
