import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel18FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel18FlatComponentChunk44

end RHP2Bridge
