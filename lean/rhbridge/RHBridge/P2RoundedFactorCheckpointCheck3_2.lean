import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk2 :
    P2RoundedFactorCheckpointData.panel3Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix8_eq :
    P2RoundedFactorCheckpointData.panel3Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk2.1

theorem panel3Prefix9_eq :
    P2RoundedFactorCheckpointData.panel3Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk2.2.1

theorem panel3Prefix10_eq :
    P2RoundedFactorCheckpointData.panel3Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk2.2.2.1

theorem panel3Prefix11_eq :
    P2RoundedFactorCheckpointData.panel3Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk2.2.2.2

end RHP2Bridge
