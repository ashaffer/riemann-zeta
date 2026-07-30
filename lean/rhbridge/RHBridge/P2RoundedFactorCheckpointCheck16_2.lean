import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk2 :
    P2RoundedFactorCheckpointData.panel16Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix8_eq :
    P2RoundedFactorCheckpointData.panel16Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk2.1

theorem panel16Prefix9_eq :
    P2RoundedFactorCheckpointData.panel16Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk2.2.1

theorem panel16Prefix10_eq :
    P2RoundedFactorCheckpointData.panel16Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk2.2.2.1

theorem panel16Prefix11_eq :
    P2RoundedFactorCheckpointData.panel16Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk2.2.2.2

end RHP2Bridge
