import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk2 :
    P2RoundedFactorCheckpointData.panel4Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix8_eq :
    P2RoundedFactorCheckpointData.panel4Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk2.1

theorem panel4Prefix9_eq :
    P2RoundedFactorCheckpointData.panel4Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk2.2.1

theorem panel4Prefix10_eq :
    P2RoundedFactorCheckpointData.panel4Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk2.2.2.1

theorem panel4Prefix11_eq :
    P2RoundedFactorCheckpointData.panel4Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk2.2.2.2

end RHP2Bridge
