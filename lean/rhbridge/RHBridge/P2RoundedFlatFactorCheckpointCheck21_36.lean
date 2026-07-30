import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel21FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel21FlatComponentChunk36

end RHP2Bridge
