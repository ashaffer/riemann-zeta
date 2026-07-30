import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk2 :
    P2RoundedFactorCheckpointData.panel0Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix8_eq :
    P2RoundedFactorCheckpointData.panel0Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk2.1

theorem panel0Prefix9_eq :
    P2RoundedFactorCheckpointData.panel0Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk2.2.1

theorem panel0Prefix10_eq :
    P2RoundedFactorCheckpointData.panel0Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk2.2.2.1

theorem panel0Prefix11_eq :
    P2RoundedFactorCheckpointData.panel0Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk2.2.2.2

end RHP2Bridge
