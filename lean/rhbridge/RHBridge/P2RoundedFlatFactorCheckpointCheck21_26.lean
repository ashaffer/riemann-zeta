import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel21FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel21FlatComponentChunk26

end RHP2Bridge
