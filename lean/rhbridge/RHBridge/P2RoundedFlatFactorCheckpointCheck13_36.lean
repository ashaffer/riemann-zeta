import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel13FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel13FlatComponentChunk36

end RHP2Bridge
