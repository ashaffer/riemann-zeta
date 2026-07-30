import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel21FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel21FlatComponentChunk28

end RHP2Bridge
