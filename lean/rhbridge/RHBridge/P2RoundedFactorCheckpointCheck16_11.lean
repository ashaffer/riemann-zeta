import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk11 :
    P2RoundedFactorCheckpointData.panel16Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix44_eq :
    P2RoundedFactorCheckpointData.panel16Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk11.1

theorem panel16Prefix45_eq :
    P2RoundedFactorCheckpointData.panel16Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk11.2.1

theorem panel16Prefix46_eq :
    P2RoundedFactorCheckpointData.panel16Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk11.2.2.1

theorem panel16Prefix47_eq :
    P2RoundedFactorCheckpointData.panel16Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk11.2.2.2

end RHP2Bridge
