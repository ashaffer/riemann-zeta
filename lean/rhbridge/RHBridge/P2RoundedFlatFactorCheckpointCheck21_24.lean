import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel21FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel21FlatComponentChunk24

end RHP2Bridge
