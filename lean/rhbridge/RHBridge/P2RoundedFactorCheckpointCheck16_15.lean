import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk15 :
    P2RoundedFactorCheckpointData.panel16Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix60_eq :
    P2RoundedFactorCheckpointData.panel16Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk15.1

theorem panel16Prefix61_eq :
    P2RoundedFactorCheckpointData.panel16Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk15.2.1

theorem panel16Prefix62_eq :
    P2RoundedFactorCheckpointData.panel16Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk15.2.2.1

theorem panel16Prefix63_eq :
    P2RoundedFactorCheckpointData.panel16Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk15.2.2.2

end RHP2Bridge
